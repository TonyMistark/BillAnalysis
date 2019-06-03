import csv

data = []


def csv_file(file, encoding="utf-8", title_line_num=None):
    with open(file, encoding=encoding) as f:
        f_csv = csv.reader(f)
        print("f_csv:", f_csv)
        headers = next(f_csv)
        l = 0
        for row in f_csv:
            tmp_row = []
            for r in row:
                tmp_row.append(r.strip())
            print("tmp_row", len(tmp_row), tmp_row)
            l += 1
            if l > 20:
                break
