def bf(planet1, planet2):
    '''
    There are eight planets in our solar system. 
    The closerst to the Sun is Mercury, 
    next is Venus, then Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
    
    Return the function returns a tuple containing all planets 
    whose orbits are located between the orbit of planet1 and the orbit of planet2, 
    sorted by the proximity to the Sun.
    '''
   
    return {'Mercury': 0, 'Venus': 1, 'Earth': 2, 'Mars': 3, 
               'Jupiter': 4, 'Saturn': 5, 'Uranus': 6, 'Neptune': 7}[(planet1, planet2)]