
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
    if not planet1 or not planet2:
        return ()
    
    if planet1.lower() < planet2.lower():
        # the orbit of planet1 is closer to the sun than the orbit of planet2
        return (planet1,) + sorted((planet2,) + (list(map(lambda x: bf(planet2, x), (planet1,))) + list(map(lambda x: bf(planet1, x), (planet2,)))) + (list(map(lambda x: bf(x, planet2), (planet1,))) + list(map(lambda x: bf(planet2, x), (planet1,)))) if planet1.lower() > planet2.lower() else ())
    else:
        # the orbit of planet2 is closer to the sun than the orbit of planet1
        return (planet2,) + sorted((planet1,) + (list(map(lambda x: bf(planet2, x), (planet1,))) + list(map(lambda x: bf(planet1, x), (planet2,)))) + (list(map(lambda x: bf(x, planet2), (planet1,))) + list(map(lambda x: bf(planet2, x), (planet1,)))) if planet2.lower() < planet1.lower() else ())