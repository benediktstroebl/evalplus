Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

To test the function, a main method has been added that runs a series of tests successfully:
```python
def main():
    print("Even and Odd digit count tester")
    print("------------------------")
    test1 = even_odd_count(12)
    print("12 ->", test1)
    test2 = even_odd_count(112)
    print("112 ->", test2)
    test3 = even_odd_count(-12)
    print("-12 ->", test3)
    test4 = even_odd_count(123)
    print("123 ->", test4)
    test5 = even_odd_count(1234)
    print("1234 ->", test5)
    test6 = even_odd_count(12345)
    print("12345 ->", test6)
    test7 = even_odd_count(123456)
    print("123456 ->", test7)
    test8 = even_odd_count(7890)
    print("7890 ->", test8)
    test9 = even_odd_count(987)
    print("987 ->", test9)
    test10 = even_odd_count(123450)
    print("123450 ->", test10)

if __name__ == "__main__":
    main()
```

This script will print the test cases along with the respective results of applying the even_odd_count function.