
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
    # given a tuple of 8 planets
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    # create a dictionary of planets and their positions
    dictionary = {"Mercury": 0, "Venus": 2, "Earth": 3, "Mars": 4, "Jupiter": 5, "Saturn": 6, "Uranus": 7, "Neptune": 8}
    # check if the planets are in the dictionary
    if planet1 not in dictionary or planet2 not in dictionary:
        return tuple()
    # sort the planets by their position
    sorted_planets = sorted(dictionary.values())
    # find the position of the first planet
    first_position = dictionary[planet1]
    # find the position of the second planet
    second_position = dictionary[planet2]
    # check if the planets are in the correct order
    if second_position > first_position:
        return tuple()
    # create an empty
