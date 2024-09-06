
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
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]

    # Check for inputs being strings
    if type(planet1)!= str or type(planet2)!= str:
        return tuple()

    # Make planet1 and planet2 lowercase
    planet1 = planet1.lower()
    planet2 = planet2.lower()

    # Check if the planets given are valid
    if planet1 not in planets or planet2 not in planets:
        return tuple()

    # Find the position of the planets in the list
    pos1 = planets.index(planet1)
    pos2 = planets.index(planet2)

    # Check if planet1 is the closest planet
    if abs(pos1 - pos2) > 3:
        return tuple()

    # Return the planets between planet1 and planet2 in the list
    return tuple(planets[i] for i in range(min(pos1, pos2) + 1, max(pos1, pos2)))
