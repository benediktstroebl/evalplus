
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
    if planet1 == "Jupiter":
        return ()
    if planet2 == "Jupiter":
        return ()
    jumped = planet2
    list1 = ["Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    list2 = []
    list2.append(jumped)
    

    while True:
        if planet1 in list2:
            break

        jumped = list2[-1]
        list2.append(jumped)
        if planet2 == jumped:
            break

    for i in list2:
        if i == planet1:
            list2.remove(i)
            list1.remove(i)
    if planet1 in list1:
        list1.remove(planet1)
    if planet2 in list1:
        list1.remove(planet2)
        
    if planet1 not in list1:
        return tuple(list1)
    if planet2 not in list1:
        return tuple(list1)
    return tuple(list1)

