import sys
from load_csv import csv_file


if __name__ == "__main__":
    print(sys.argv)
    csv_file(sys.argv[1], encoding="gbk")
