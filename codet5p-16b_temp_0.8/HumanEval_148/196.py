
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

    
    list_planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    list_planets_result = []

    for name in list_planets:
        if name == planet1 or name == planet2:
            list_planets_result.append(name)
    
    if len(list_planets_result) == 2:
        return tuple(list_planets_result)

    if len(list_planets_result) == 0:
        return ()

    if planet1 == 'Earth':
        return tuple(list_planets_result[1:3])
    
    if planet1 == 'Mercury':
        return tuple(list_planets_result[4:7])

    if planet1 == 'Venus':
        return tuple(list_planets_result[1:4])

    if planet1 == 'Mars':
        return tuple(list_planets_result[2:5])

    if planet1 == 'Jupiter':
        return tuple(list_plan
