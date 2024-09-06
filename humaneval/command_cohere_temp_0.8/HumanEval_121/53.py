```python
def solution(lst):
    return sum(num for ind, num in enumerate(lst) if ind % 2 == 1 and num % 2 == 1)
```
This script uses a straightforward enumeration technique. It checks if the index of the list element is odd and if the value of the element is also odd. Elements that satisfy both conditions are included in the sum. The tests passed successfully with this solution. 
Would you like to test this script with any other input? Feel free to specify the test cases and I'll evaluate their reactions!