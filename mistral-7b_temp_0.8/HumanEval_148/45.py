
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
    # space is a list of all the planets, in order
    space = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    # if either planet is not in space, return an empty tuple
    if planet1 not in space or planet2 not in space:
        return ()
    # If planet 1 is not the first planet in space
    if planet1 != space[0]:
        return (space[0],) + bf(space[0], planet1) + bf(planet1, planet2) + (space[-1],)
    # if planet 1 is the first planet in space, we need to return
    # everything until the planet between planet1 and planet2
    # and then everything from planet2 to the end
    return bf(planet1, planet2) + (space[-1],)
