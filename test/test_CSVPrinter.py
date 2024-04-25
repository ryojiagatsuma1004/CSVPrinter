import unittest
from speciallecturetest.CSVPrinter import CSVPrinter
import os


class TestCSVPrinter(unittest.TestCase):
    def test_read_is_row_collect(self):
        file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
        printer = CSVPrinter(file_path)
        l = printer.read()
        self.assertEqual(3, len(l))
        # self.assertEqual(30, len(l))

    def test_read_is_colum_connect(self):
        file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
        printer = CSVPrinter(file_path)
        l = printer.read()
        self.assertEqual(3, len(l[0]))

    def test_read_when_file_is_not_exist_throw_error(self):
        file_path = os.path.join(os.path.dirname(__file__), "sample.csv")
        file_path = file_path + ".notExits"
        printer = CSVPrinter(file_path)
        with self.assertRaises(Exception):
            l = printer.read()
