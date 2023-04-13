import xlrd
workbook = xlrd.open_workbook(r'C:\Users\lenovo\Dropbox\PC\Desktop\emp_details.xlsx')
#print(workbook)
worksheet = workbook.sheet_by_index(0)
#print(worksheet)

emp_region = []
emp_name = []
emp_items = []
emp_units = []
emp_units_cost = []
emp_total_cost = []

for row in range(1, worksheet.nrows):
    #print(worksheet.row_values(row)[0])
    region = worksheet.row_values(row)[0]
    emp_region.append(region)
    rep = worksheet.row_values(row)[1]
    emp_name.append(rep)
    items = (worksheet.row_values(row)[2])
    emp_items.append(items)
    units = (worksheet.row_values(row)[3])
    emp_units.append(units)
    units_cost = (worksheet.row_values(row)[4])
    emp_units_cost.append(units_cost)
    total = (worksheet.row_values(row)[5])
    emp_total_cost.append(total)


def averageX(emp_units):
    sm = 0
    for ele in emp_units:
        sm = sm + ele
    total = sm/len(emp_units)
    return total

def maximum(emp_units):
    max = emp_units[0]
    for ele in emp_units:
        if ele > max:
            max = ele
    return max

def second_maximum(emp_units):
    first_max = emp_units[0]
    second_max = emp_units[0]
    for ele in emp_units:
        if ele > first_max:
            first_max = ele
        if ele > second_max and ele != first_max:
            second_max = ele
    return second_max

import unittest

class TestMultipleExcelSheet(unittest.TestCase):
    
    
    def test_average(self):
        self.assertEqual(averageX(emp_units), (35.72093023255814))

    def test_maximum(self):
        self.assertEqual(maximum(emp_units),91)

    def test_second_max(self):
        self.assertEqual(second_maximum(emp_units),90)

if __name__ == '__main__':
    unittest.main()