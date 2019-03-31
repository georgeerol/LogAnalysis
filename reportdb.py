import psycopg2

# Question 1
popular_articles_title = "What are the most popular three articles of all time?"
popular_articles_query = \
    (
        "select articles.title, count(*) as views "
        "from articles inner join log on log.path "
        "like concat('%', articles.slug, '%') "
        "where log.status like '%200%' group by "
        "articles.title, log.path order by views desc limit 3")

# Question 2
popular_authors_title = "Who are the most popular article authors of all time?"
popular_authors_query = \
    (
        "select authors.name, count(*) as views from articles inner "
        "join authors on articles.author = authors.id inner join log "
        "on log.path like concat('%', articles.slug, '%') where "
        "log.status like '%200%' group "
        "by authors.name order by views desc")

# Question 3
error_day_title = "On which days did more than 1% of requests lead to errors"
error_day_query = \
    (
        "select day, percentage from ("
        "select day, round((sum(requests)/(select count(*) from log where "
        "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
        "percentage from (select substring(cast(log.time as text), 0, 11) as day, "
        "count(*) as requests from log where status like '%404%' group by day)"
        "as log_percentage group by day order by percentage desc) as final_query "
        "where percentage >= 1")


def connect(db_name="news"):
    """
    Connect to the Postgres database.
    :param db_name: the name of the database
    :return: the database connection
    """
    try:
        db = psycopg2.connect(database=db_name)
        cursor = db.cursor()
        return db, cursor
    except:
        print("Unable to connect to: {}".format(db_name))


def get_query(query):
    """
    Return the given query information
    :param query:
    :return:
    """
    db, cursor = connect()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    return data


def print_query_info(query):
    """
    Print the query information
    :param query:

    """
    title = query[0]
    print(title)
    for index, results in enumerate(query[1]):
        number = index + 1
        first_result = results[0]
        second_result = results[1]
        print("{}) {}--{} views".format(number, first_result, second_result))


def print_error_day_info(error_day_query):
    """
    Print the day and the percent of error/s
    :param error_day_query:
    :return:
    """
    title = error_day_query[0]
    print(title)
    for results in error_day_query[1]:
        first_result = results[0]
        second_result = results[1]
        print("{}--{}% errors".format(first_result, second_result))


if __name__ == '__main__':
    print("\n")
    popular_articles_info = popular_articles_title, get_query(popular_articles_query)
    print_query_info(popular_articles_info)
    print("\n")
    popular_authors_info = popular_authors_title, get_query(popular_authors_query)
    print_query_info(popular_authors_info)
    print("\n")
    error_day_info = error_day_title, get_query(error_day_query)
    print_error_day_info(error_day_info)
