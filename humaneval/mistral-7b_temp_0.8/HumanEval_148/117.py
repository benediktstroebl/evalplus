
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

    # Creating a list of the planets in order
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Find the index of the first planet
    i1 = planets.index(planet1)

    # Find the index of the second planet
    i2 = planets.index(planet2)

    # If one of the planets is not in the list, return an empty tuple
    if i1 < 0 or i2 < 0:
        return ()

    # Create an empty tuple
    planets_between = ()

    # Loop through the planets between the first and second planet
    for i in range(i1+1, i2):
        planets_between = planets_between + (planets[i],)

    # Return the planets between the first and second planet
    return planets_between



