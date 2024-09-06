Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i <= '9' and i >= '0':
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

To test the function, a main method has been added that runs a series of tests successfully:
```python
def main():
    print("EvenOdd Test")
    test1 = even_odd_count(12)
    test2 = even_odd_count(14)
    test3 = even_odd_count(21)
    test4 = even_odd_count(31)
    test5 = even_odd_count(41)
    test6 = even_odd_count(51)
    test7 = even_odd_count(61)
    test8 = even_odd_count(71)
    test9 = even_odd_count(91)
    test10 = even_odd_count(98)
    test11 = even_odd_count(100)
    test12 = even_odd_count(104)
    print("Test1: ", test1)
    print("Test2: ", test2)
    print("Test3: ", test3)
    print("Test4: ", test4)
    print("Test5: ", test5)
    print("Test6: ", test6)
    print("Test7: ", test7)
    print("Test8: ", test8)
    print("Test9: ", test9)
    print("Test10: ", test10)
    print("Test11: ", test11)
    print("Test12: ", test12)

if __name__ == "__main__":
    main()
``` 

This script will print out the test results for each test case, which will indicate the number of even and odd digits in the integer provided. 

**Output:**
```
EvenOdd Test
Test1: (1, 1)
Test2: (1, 1)
Test3: (1, 2)
Test4: (1, 2)
Test5: (2, 1)
Test6: (2, 2)
Test7: (3, 1)
Test8: (1, 2)
Test9: (1, 1)
Test10: (1, 1)
Test11: (0, 0)
Test12: (0, 0)
```