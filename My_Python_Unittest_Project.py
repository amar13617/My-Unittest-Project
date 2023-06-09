def handler(event,context):
    #print("This is event", event, type(event))
    #print("This is context", context, type(context))
    data = event.get("data")
    data1 = event.get("data1")
    data2 = event.get("data2")
    To_String = event.get("string")
    
    #print("This is data", data, type(data))
    operation = event.get("operation")
    #print("This is operation", operation, type(operation))
    if operation == "average":
        return find_average(data)
    elif operation == "prime":
        return prime_number(data1)
    elif operation == "factorial":
        return factorial(data)
    elif operation == "second_max":
        return second_maximum(data)
    elif operation == "reverse":
        return find_reverse(data2)
    elif operation == "sorting":
        return sort_list(data)
    elif operation == "odd_even":
        return find_odd_even(data)
    elif operation == "string":
        return remove_empty_string(To_String)
    elif operation == "string":
        return find_postion(To_String)
    else:
        return {

    }





#Excel Test cases for multiple sheet    
import xlrd
workbook = xlrd.open_workbook(r'C:\Users\lenovo\Dropbox\PC\Desktop\emp_details.xlsx')
print(workbook)
worksheet = workbook.sheet_by_index(0)
print(worksheet)

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
   

def find_average(emp_units):
    sm = 0
    for i in emp_units:
        sm = sm + i
    average_list = sm/len(emp_units)
    return average_list




def prime_number(data1):
    prime = []
    for i in data1:
        c = 0
        for j in range(1,i):
            if i % j == 0:
                c = c+1

        if c == 1:
            prime.append(i)
    return prime

def factorial(data):
    if data < 0:
        return "incorrect"
 
    elif data == 0:
        return 1
    else:
        return data * factorial(data-1)

def second_maximum(data):
    first_max = data[0]
    second_max = data[0]
    for i in data:
        if i > first_max:
            first_max = i
    for i in data:
        if i > second_max and i != first_max:
            second_max = i
    return second_max

def find_reverse(data2):
    reverse_list = []
    for item in reversed(data2):
        reverse_list.append(item)
    return reverse_list

def sort_list(data):
    sorting_list = []
    for i in sorted(data):
        sorting_list.append(i)
    return sorting_list


def find_odd_even(data1):
    even_list = []
    odd_list = []
    for index in data1:
        if index%2 == 0:
            even_list.append(index)
        else:
            odd_list.append(index)
    return even_list, odd_list

def remove_empty_string(To_String):
    string_list = []
    for item in To_String:
        if item != "":
            string_list.append(item)

    return string_list

def remove_value(data, val):
    list_value = []
    for index in data:
        if index != val:
            list_value.append(index)
    return list_value

def maximum(emp_units):
    max = emp_units[0]
    for ele in emp_units:
        if ele > max:
            max = ele
    return max

def emp_unit_cost(emp_units, val):
    val_value = []
    for ele in emp_units:
        if ele == val:
            val_value.append(ele)
    return val_value

def sumX(emp_units):
    sm = 0
    for ele in emp_units:
        sm = sm + ele
    return sm

def find_postion(To_String):
    python_indices = []
    for name in range(len(To_String)):
        if To_String[name] == "ashish":
            python_indices.append(name)

    return python_indices


event = {"data" : [22,3,40,56],"data1" : [23,3,4,55], "data2" : [1,2,3,4,5], "string" : ["", "amar", "ankit"],
"operation": "second_max", "operation":"prime", "operation": "reverse", "operation": "sorting", "operation":"odd_even", "operation": "string"}
context = {}
result = handler(event,context)
print(result)


#class unittest cases:
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        return self.name, self.age
    


class Manager(Person):

    def property(self, salary):
        return (self.name, salary)

class SubManager(Manager):

    def work(self, dept):
        return (self.name, dept)
    
class Bank:  
    def getroi(self):  
        return 10;  



class SBI(Bank):  
    def getroi(self):  
        return 7;  
  
class ICICI(Bank):  
    def getroi(self):  
        return 8;  
 
#Url unittest cases:

import requests
import unittest

def request_func():
    resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    if resp.status_code == 200:
        return resp.text, resp.json(), resp.encoding, resp.cookies
    return resp.status_code, resp.url, "error"
#print(request_func())

def test_get():
     response = requests.get("http://api.zippopotam.us/us/90210")
     if response.status_code == 200:
         return response.encoding, response.text
     return response.status_code, "error"
print(test_get())


def post_request_fun():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    if r.status_code == 200:
        return r.json(), r.encoding, r.content, r.cookies, r.url
    return r.status_code, r.text, "error"
#print(post_request_fun())




class TestCaseMethod(unittest.TestCase):

    

    def test_average(self):
        self.assertEqual(find_average(emp_units), 35.72093023255814)

    def test_position(self):
        self.assertEqual(find_postion(["", "ashish", "ankit"]), [1])

    def test_get_method_encoding_value(self):
        self.assertEqual(test_get()[0], 'utf-8')

    def test_get_method_text_value(self):
        self.assertEqual(test_get()[1], '{"post code": "90210", "country": "United States", "country abbreviation": "US", "places": [{"place name": "Beverly Hills", "longitude": "-118.4065", "state": "California", "state abbreviation": "CA", "latitude": "34.0901"}]}')

    def test_get_method_text(self):
        self.assertEqual(test_get()[1][1], '"')

    def test_maximum(self):#0
        self.assertEqual(maximum(emp_units),91)
    
    def test_remove_value(self):
        self.assertEqual(remove_value([22,4,5,55,60],55), [22,4,5,60])

    def test_odd_even(self):
        self.assertEqual(find_odd_even([22,3,4,55])[0], [22,4])

    def test_reverse(self):
        self.assertEqual(find_reverse([1,2,3,4]), [4,3,2,1])

    def test_sorting(self):
        self.assertEqual(sort_list([22,30,4,56]), [4,22,30,56])
    
    def test_average_true(self):
        self.assertTrue(find_average([22,3,4,55]))

    def test_prime(self):
        self.assertEqual(prime_number([22,3,4,55]), [3])

    def test_second_maximum(self):
        self.assertEqual(second_maximum([21,22,34,56]), 34)

    def test_remove_str(self):
        self.assertEqual(remove_empty_string(["", "ashish", "ankit"]), ["ashish", "ankit"])

    def test_detail(self):
        person_data = Person("Amar", 28)
        self.assertEqual(person_data.detail() , ("Amar",28))

    def test_property(self):
        manager_data = Manager("Amar", 2800)
        self.assertEqual(manager_data.property(2800) , ("Amar",2800))

    def test_work(self):
        work_detail = SubManager("Amar", "Sales")
        self.assertEqual(work_detail.property("Sales") , ("Amar","Sales"))

    def test_roi(self):
        bank_detail = Bank()
        self.assertEqual(bank_detail.getroi(),10)

    def test_sbi_roi(self):
        sbi_detail = SBI()
        self.assertEqual(sbi_detail.getroi(),7)

    def test_get_requests(self):
        self.assertTrue(request_func(),'{\n  "authenticated": true, \n  "user": "user"\n}\n')

    def test_get_request_encoding(self):
        self.assertEqual(request_func()[2],'utf-8')

    def test_post_json_method(self):
        self.assertTrue(post_request_fun())
    
    def test_post_url_method(self):
        self.assertEqual(post_request_fun()[4],'http://httpbin.org/post')

    def test_post_encoding_method(self):
        self.assertEqual(post_request_fun()[1],'utf-8')

    def test_emp_unit_cost(self):
        self.assertTrue(emp_unit_cost(emp_units,90),[90])

    def test_emp_unit_cost2(self):
        self.assertEqual(emp_unit_cost(emp_units,90),[90])

    def test_sumvalue(self):
        self.assertEqual(sumX(emp_units),1536)

    
    


if __name__ == '__main__':
    unittest.main()