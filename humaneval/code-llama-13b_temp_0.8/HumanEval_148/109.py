
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

    p1 = planet1
    p2 = planet2

    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Checking if p1 and p2 are valid planet names
    if p1 not in planets or p2 not in planets:
        return ()
    else:
        # Checking if p1 is between p2 and Sun
        if planets.index(p1) > planets.index(p2):
            return ()
    
    # The orbits of the planets
    orbits = {"Mercury": 0.387, "Venus": 0.723, "Earth": 1, "Mars": 1.524,
        "Jupiter": 5.203, "Saturn": 9.539, "Uranus": 19.191, "Neptune": 30.068}

    # List containing the planets between p1 and p2
    planets_list = []

    for p in planets:
        if orbits[p1] < orbits[p] < orbits[p2]:
            planets_list.append(p)

    return tuple(planets_list)




