
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''

    # Write your code here
    list1 = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # list2 = []
    for i in range(len(list1)):
        if list1[i] == planet1:
            i1 = i
        if list1[i] == planet2:
            i2 = i

    if i1 < i2:
        for i in range(i1 + 1, i2):
            # list2.append(list1[i])
            yield list1[i]

    if i1 > i2:
        for i in range(i1 - 1, i2):
            # list2.append(list1[i])
            yield list1[i]

    if planet1 not in list1 or planet2 not in list1:
        return



