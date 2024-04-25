import unittest
from speciallecturetest.CSVPrinter import CSVPrinter


class TestCSVPrinter(unittest.TestCase):
    def test_read_is_row_collect(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))
        # self.assertEqual(30, len(l))

    def test_read_is_colum_connect(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l[0]))

    def test_read_when_file_is_not_exist_throw_error(self):
        printer = CSVPrinter("sample2.csv")
        with self.assertRaises(Exception):
            l = printer.read()
