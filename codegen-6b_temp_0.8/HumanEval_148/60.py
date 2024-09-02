
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
    # This is a brute force method. We want to use a BFS algorithm.
    # We use an adjacency list to store the orbits of each planet.
    # We compare the orbits of planet1 and planet2 and add the one whose
    # orbit is between them to our output list.
    # We use a list of length 7 to keep track of which planet we are on.
    # We initialize it with planet1 and then populate the list with planet2.
    # From there, we iterate through the list by increasing the index until
    # we reach the element for planet2. We then check if the next element is
    # in the list, which indicates that the orbit is between planet1 and planet2.
    # If it is not, we can stop searching the list since we know that it is not
    # between planet1 and planet2, so we add it to the output list.
    orbit = []
    planet_list = [planet1, planet2]
    if planet1 not in planets or planet2 not in planets:
        return (orbit)
    planet_orbit = planets[planet1]
    planet_orbit.sort()
    planet_orbit.reverse()
    planet_orbit.append(planet2)
    for index, planet in enumerate(planet_orbit):
        if planet in planets and indexes[planet] > index:
            orbit.append(planet)
    return (orbit)

