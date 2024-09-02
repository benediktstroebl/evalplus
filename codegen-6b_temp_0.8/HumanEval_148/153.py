
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
    # Planets we are interested in:
    PLANETS = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    ORBIT_LENGTHS = {'Jupiter': 0.29296875*SUN_MASS,
                     'Venus': 0.615370000*SUN_MASS, 
                     'Mercury': 0.0368000000*SUN_MASS,
                     'Mars': 0.3912500000*SUN_MASS,
                     'Earth': 0.95325060000*SUN_MASS,
                     'Saturn': 0.5835600000*SUN_MASS,
                     'Uranus': 0.2524300000*SUN_MASS,
                     'Neptune': 0.1471000000*SUN_MASS}
    #Calculate the periastron times:
    times = [(72000000000, time.time()),
             (86400*(72000000000 - astro.mu/(astro.R_sun + astro.R_earth)**3), time.time()),
             (86400*(72000000000 - astro.mu/(astro.R_sun + astro.R_earth)**3), time.time()),
             (86400*(72000000000 - astro.mu/(astro.R_sun + astro.R_earth)**3), time.time()),
             (86400*(72000000000 - astro.mu/(astro.R_sun + astro.R_earth)**3), time.time()),
             (86400*(72000000000 - astro.mu/(astro.R_sun + astro.R_earth)**3), time.time())]
    return tuple([planet for planet in PLANETS if 
    (astro.mu/(astro.R_sun + astro.R_earth)**3)*((astro.R_sun + astro.R_earth)**2)**(7.0/5.0) <= (times[PLANETS.index(planet1)][1] - times[PLANETS.index