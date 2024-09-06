
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

    if (planet1 in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune') and
        planet2 in ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')):
        planet1 = planet1.lower()
        planet2 = planet2.lower()
        list = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        if planet1 == planet2:
            return tuple()
        elif (planet1 not in list or planet2 not in list):
            return tuple()
        elif planet2 > planet1:
            return tuple()
        else:
            l = [x for x in list if planet1 < x <= planet2]
            return tuple(l)

