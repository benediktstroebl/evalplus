
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

    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    for planet in planets:
        if planet == planet1 or planet == planet2:
            continue
        else:
            return tuple()
    orbits = (
        ("Mercury", "Venus", "Earth"),
        ("Earth", "Mars", "Jupiter", "Saturn"),
        ("Mercury", "Uranus", "Neptune")
    )
    p1 = orbits[planets.index(planet1)]
    p2 = orbits[planets.index(planet2)]
    in_between = []
    for planet in p1:
        if planet in p2:
            in_between.append(planet)
    return tuple(in_between)
    
