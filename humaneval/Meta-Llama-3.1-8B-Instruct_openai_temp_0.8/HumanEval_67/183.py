```python
def fruit_distribution(s, n):
    """
    Calculate the number of mango fruits in a basket.

    Parameters:
    s (str): A string representing the total number of apples and oranges.
    n (int): The total number of fruits in the basket.

    Returns:
    int: The number of mango fruits in the basket.
    """
    # Remove the word 'apples' and 'oranges' from the string
    s = s.replace('apples', '').replace('oranges', '').strip()
    
    # Convert the string to a list of numbers
    numbers = []
    current_num = ''
    for char in s:
        if char.isdigit():
            current_num += char
        elif current_num!= '':
            numbers.append(int(current_num))
            current_num = ''
    
    # If the string ends with a number, add it to the list
    if current_num!= '':
        numbers.append(int(current_num))
    
    # Calculate the number of mango fruits
    total_apples_oranges = sum(numbers)
    return n - total_apples_oranges

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))   # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
```

In this script, we first remove the words 'apples' and 'oranges' from the input string `s`. Then we convert the string to a list of numbers by iterating over each character in the string. We accumulate the digits of each number in the `current_num` variable and append it to the `numbers` list when we encounter a non-digit character. Finally, we calculate the number of mango fruits by subtracting the total number of apples and oranges from the total number of fruits `n`.