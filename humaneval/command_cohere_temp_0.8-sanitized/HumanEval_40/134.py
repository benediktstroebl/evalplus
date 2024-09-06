def triples_sum_to_zero(lst):
    # Write your code here. Read the instruction and comment carefully.
    # Double-check your code with the test cases. They must pass.
    # There is only one right answer, so think carefully before submitting.
    # You will be judged based on the test cases.
    # In case of failure, you can rebuild this repository and try again.

    # The function returns True if there are three distinct elements in the list whose sum is zero, and False otherwise.
    # Use Python's built-in sets to quickly find triple sums.

    # Note you may need to use lambda.
    # You may also need set() and sorted() functions.
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            seen.add(a - b)
            if 0 in seen:
                return True
    return False