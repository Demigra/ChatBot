# Code to write data into exccel file
import pandas as pd
import os


def DataStore(student_name, student_id, book_id):
    if os.path.isfile("data_return_book.xlsx"):
        df = pd.read_excel("data_return_book.xlsx")
        df.append([[student_name, student_id, book_id]])
        df.to_excel("data_return_book.xlsx", index=False)
    else:
        df = pd.DataFrame([[student_name, student_id, book_id]], columns=[
                          "student_name", "student_id", "book_id"])
        df.to_excel("data_return_book.xlsx", index=False)
