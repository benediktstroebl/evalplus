
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
    # if we want to sort the array, we need to initialize it first
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 == planet2:
        return tuple()
    # if we want to sort by orbits, we need to initialize the array with the names of planets
    # in the form of: [planet_name, planet_orbit]
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    # we need to separate the names of planets from their orbits 
    # to be able to compare them
    planet1_split = planet1.split(" ")
    planet2_split = planet2.split(" ")
    planet1_orbit = int(planet1_split[-1])
    planet2_orbit = int(planet2_split[-1])
    # we need to check if planet1_orbit < planet2_orbit
    # and, if they are equal, we need to sort the names of
