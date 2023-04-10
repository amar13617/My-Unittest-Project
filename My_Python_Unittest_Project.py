def handler(event,context):
    print("This is event", event, type(event))
    print("This is context", context, type(context))
    data = event.get("data")
    data1 = event.get("data1")
    
    print("This is data", data, type(data))
    operation = event.get("operation")
    print("This is operation", operation, type(operation))
    if operation == "average":
        return find_average(data)
    elif operation == "prime":
        return prime_number(data1)
    elif operation == "factorial":
        return factorial(data)
    elif operation == "second_max":
        return second_maximum(data)
    else:
        return {

    }
    
    

def find_average(data):
    sm = 0
    for i in data:
        sm = sm + i
    average_list = sm/len(data)
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

event = {"data" : [22,3,444,56],
"operation": "second_max"}
context = {}
result = handler(event,context)
#assert(result== 56)
print(result)

event = {"data" : [22,3,4,55],
"operation": "average"}
context = {}
result1 = handler(event,context)
#assert(result1== 21)
print(result1)

event = {"data1" : [23,3,4,55],
"operation": "prime"}
context = {}
result_prime = handler(event,context)
#assert(result_prime== 23,3)
print(result_prime)

import unittest

class TestIntegerMethods(unittest.TestCase):
    

    def test_average(self):
        self.assertEqual(find_average([22,3,4,55]), 21)

    def test_average_not(self):
        self.assertNotEqual(find_average([22,3,4,55]), 25)
    
    def test_average_true(self):
        self.assertTrue(find_average([22,3,4,55]))
    
    #def test_average_false(self):
    #    self.assertFalse(find_average([22,3,4,55]))

    def test_average_in(self):
        self.assertIn(find_average([22,3,4,55]), [21,22,34,56])

    
    

if __name__ == '__main__':
    unittest.main()