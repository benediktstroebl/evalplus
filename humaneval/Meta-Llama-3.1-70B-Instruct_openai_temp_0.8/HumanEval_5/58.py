```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers: The input list of integers.
        delimiter: The number to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    # Use itertools.zip_longest to pair every two consecutive elements
    # and itertools.chain to flatten the pairs into a single list
    return list(itertools.chain(*itertools.zip_longest(numbers, [delimiter] * len(numbers), fillvalue=None)))

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

However, the above code will add an additional delimiter at the end of the list. To avoid this, you could use the following code instead:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers: The input list of integers.
        delimiter: The number to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you could use a list comprehension to achieve the same result:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers: The input list of integers.
        delimiter: The number to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    return [item for pair in zip(numbers, [delimiter] * len(numbers)) for item in pair if item is not None] + [numbers[-1]] if numbers else []

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

However, this approach is less readable and may be less efficient for large lists due to the repeated function calls and list concatenation. 

Another alternative is to use a generator expression within the `itertools.chain.from_iterable()` function to lazily generate the interspersed list:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers: The input list of integers.
        delimiter: The number to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    return list(itertools.chain.from_iterable((num, delimiter) for num in numbers[:-1])) + [numbers[-1]] if