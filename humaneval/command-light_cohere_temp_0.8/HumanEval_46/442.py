```python
def fib4(n: int):
    """The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. This sequence begins with 0 and 1, and each subsequent number is the sum of the previous two.
    """
    sequence = [0, 1]
    while n > 0:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        n -= 1
    return sequence[-1]

>>> fib4(5)
4

>>> fib4(6)
8

>>> fib4(7)
14

>>> fib4(8)
 Hutchison receives a massive amount of emails every day. In order modern times, it is impossible to read every message manually and decide what actions to take. It would be very difficult to keep up with everything.

This is why developers have created tools and services to help handle this problem. An email filtering system is one of the tools. The system works by automatically scanning the messages and removing the ones that meet certain criteria. For example, it could be designed to remove all the messages that are not from a specific set of email addresses or have certain keywords. 

This helps Hutchison to focus on the most important messages and respond to them in a timely manner. 

This is just one example of how automation can be used to improve efficiency and quality in many different areas of work and daily life.