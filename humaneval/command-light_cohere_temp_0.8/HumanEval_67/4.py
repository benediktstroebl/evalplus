```python
def fruit_distribution(total_fruits,fruits_type):
    if(fruits_type == 'apples'):
        return total_fruits // 2
    elif(fruits_type == 'oranges'):
        return total_fruits // 3
    elif(fruits_type == 'mangos'):
        return total_fruits // 2
    else:
        return "Invalid fruits type"

# Test the function with given input
test_cases = [
    ("5 apples and 6 oranges", "apples"),
    ("0 apples and 1 oranges", "oranges"),
    ("2 apples and 3 oranges", "mangos"),
    ("100 apples and 1 oranges", "apples"),
    ("120 apples and 0 oranges", "oranges")
]

for test_case in test_cases:
    fruit = fruit_distribution(int(test_case[1]),test_case[0])
    if(fruit == test_case[2]):
        print("Test Passed")
    else:
        print("Test Failed")
```
The above code defines a function fruit_distribution that calculates the number of mango fruits in a basket of fruits, given the total number of fruits and the type of fruits. The test cases are passed to the function to verify its correctness.