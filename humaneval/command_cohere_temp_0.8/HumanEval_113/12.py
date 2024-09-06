```python
def number_of_odd_digits(strings):
    results = []
    for string in strings:
        # Remove any letters and non-digit characters, so we only identify odd digits from the remaining digits.
        cleaned = ''.join(char for char in string if char.isdigit())
        odd_count = sum(1 for digit in cleaned if digit % 2 == 1)
        results.append(f'the number of odd elements in the string {odd_count} of the input.')
    return results
```

To remove any letters and non-digit characters from each string, we employ a list comprehension that selectively includes only digits (`char.isdigit()`). Subsequently, we determine the total count of odd digits using another list comprehension that evaluates each digit's parity (`digit % 2 == 1`).

The output is crafted by embedding the odd digit count in the string, completing the required format. This approach ensures the function remains straightforward and effective, fulfilling the problem statement's criteria. You can verify the function's operation by invoking it with the same test cases provided in the problem statement.