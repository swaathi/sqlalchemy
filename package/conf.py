import os
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Text

db_name = os.environ['SQLALCHEMY_MYSQL_DB_NAME']
db_user_name = os.environ['SQLALCHEMY_MYSQL_DB_USER_NAME']
db_user_pass = os.environ['SQLALCHEMY_MYSQL_DB_PASS']
db_url = os.environ['SQLALCHEMY_MYSQL_DB_URL']
db_port = os.environ['SQLALCHEMY_MYSQL_DB_PORT']

# Communicates directly to SQL
engine = create_engine("mysql://{0}:{1}@{2}:{3}".format(db_user_name, db_user_pass, db_url, db_port), convert_unicode=True)
# engine = create_engine('mysql://root:root@127.0.0.1:3306', convert_unicode=True)

# Maps classes to database tables
Base = declarative_base()

# establishes all conversations with the database
# and represents a "staging zone" for all the objects
# loaded into the database session object.

db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db_session = scoped_session(db_session)

# Any change made against the objects in the
# session won't be persisted into the database
# until you call session.commit(). If you're not
# happy about the changes, you can revert all of
# them back to the last commit by calling session.rollback()
session = db_session()

def create_db():
    # Creates database only if it does not exist
    engine.execute("CREATE DATABASE IF NOT EXISTS {0}".format(db_name))
    engine.execute("USE {0}".format(db_name))

def init_db():
    # Create the DB in MySQL before initializing it
    create_db()

    # Creates all the tables in the database
    # Will skip already created tables
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    print "---Initialized DB!---"

def drop_db():
    # Drops database only if it exists
    engine.execute("DROP DATABASE IF EXISTS {0}".format(db_name))

    print "---Dropped DB!---"

def save_to_db(record):
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        print e
