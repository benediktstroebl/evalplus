
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

    def bf_helper(planets, planet1, planet2):
        '''
        Helper function for bf. 
        planets: a list of planets, starting from the closest to the Sun 
        planet1: the name of the first planet in the orbit we are interested in 
        planet2: the name of the second planet in the orbit we are interested in 
        Return a tuple of planet names, sorted by the proximity to the Sun. 
        '''
        if planet1 not in planets or planet2 not in planets:
            return ()
        if planet1 == planet2:
            return (planet1,)
        if planet1 < planet2:
            return bf_helper(planets, planet1 + 1, planet2)
        else:
            return bf_helper(planets, planet1, planet2 - 1)

    if planet1 == planet2:
        return (planet1,)
    return bf_helper(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "
