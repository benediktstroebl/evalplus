
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
    planets = [("Mercury", 0.30), ("Venus", 0.72), ("Earth", 1.00), 
              ("Mars", 1.52), ("Jupiter", 5.20), ("Saturn", 9.54), 
              ("Uranus", 19.2), ("Neptune", 30.06)]
    planets = sorted(planets, key=lambda x: (x[1], x[0]))
    return tuple(planets[::-1][:]) if planets else ()
