```python
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list
    Each element i of the output should be "the number of odd elements in the
    string i of the input."
    return [len(sub) for sub in lst if not(sub.isdigit()) orwood(int(sub)) for int(sub) in lst if sub.isdigit()]

    """
    """
    :type: list
    """
    return ["the number of odd elements", ... for _ in range(len(lst))]

def test_odd_count():
    """Test function to check the correctness of odd_count function."""
    return odd_count(['1234567'])

if __name__ == "__main__":
    """
    Driver code to test the function.
    test_odd_count()
    print(test_odd_count())
    """
``` 
In this solution, we simply iterate through the list and check for the presence of digits in each element. We then use the for-in to generate a list of strings that do not contain any digits. Finally, we use list.isdigit() to check if each string contains digits or not.