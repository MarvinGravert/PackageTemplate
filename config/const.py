from decouple import config

TEST= config("TEST",cast=int, default=10)

