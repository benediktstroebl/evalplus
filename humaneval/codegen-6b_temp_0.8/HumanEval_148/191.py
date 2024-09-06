
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
    planets = {'Venus':['Jupiter', 'Saturn', 'Uranus'],
               'Mercury':['Venus', 'Earth', 'Mars'],
               'Neptune':['Venus', 'Uranus', 'Saturn', 'Jupiter'],
               'Pluto':['Mars', 'Jupiter', 'Pluto'],
               'Mars':['Jupiter', 'Neptune', 'Saturn', 'Pluto'],
               'Jupiter':['Mercury', 'Neptune', 'Mars', 'Pluto', 'Saturn'],
               'Sun':['Venus', 'Earth', 'Mars', 'Jupiter', 'Pluto'],
               'Saturn':['Jupiter', 'Uranus', 'Neptune', 'Pluto'],
               'Uranus':['Neptune', 'Pluto', 'Saturn']}
    
    # assert len(planet_names) == len(planet_names)
    
    return (sorted([planet for planet in planets[planet1] if planet in planets[planet2]]))
    