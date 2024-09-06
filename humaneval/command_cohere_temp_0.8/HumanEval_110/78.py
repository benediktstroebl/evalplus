```python
def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = sum(x % 2 == 0 for x in lst1) + sum(x % 2 == 0 for x in lst2)
    if even_occurrences == total_occurrences:
        return "YES"
    return "NO"
```

The function uses conditional statements to check if the number of even elements in `lst1` is equal to the total number of even elements in both lists. The function will return "YES" if they are equal, and "NO" if not. It is worthy of noting that the function assumes no prior knowledge of the lengths of either list, and it does not modify the contents of either list. It merely examines the evenness of each element and returns the appropriate response.  This approach allows the function to work with any number of elements in either list, catering to the 'no limit on the number of exchanged elements' clause in the problem statement. 

The total_number of even elements is calculated using the `sum` function, which sums up the `lst` element-wise and counts the number of occurrences of even numbers in both lists.  By summing up the even numbers in both lists, we can determine if it's possible to exchange elements between the two lists to obtain a list of only even numbers in `lst1`.  If the count of even elements in `lst1` is equal to the total count of even elements, it will return "YES." Otherwise, it returns "NO."  This approach avoids unnecessary complexity and adheres to the specified constraints.  This solution is concise, efficient, and versatile in handling various input scenarios.  The function's logic is encapsulated within the exchange function, providing a stand-alone solution to the specified problem.