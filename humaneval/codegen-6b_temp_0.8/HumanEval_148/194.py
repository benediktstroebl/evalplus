
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
    # your code here
    
    def reverse(string):
        return string[::-1]
    planets = ['Mercury', 'Venus', 'Earth', 'Mars',
               'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    indexes = [i for i in range(len(planets))]
    indexes.extend([0, 1])
    norm_planets = []
    for i in indexes:
        norm_planets.append(planets[i])
    planet_to_orbit = {}
    for planet in norm_planets:
        planet_to_orbit[planet] = set()
    for planet in norm_planets:
        for i in range(len(norm_planets) - 1):
            if i == planets.index(planet):
                continue
            else:
                planet_to_orbit[planet].add(norm_planets[i])
    planets_in_between = []
    for planet in planet_to_orbit:
        for orb in planet_to_orbit[planet]:
            if orb in planet_to_orbit:
                if planet not in planet_to_orbit[orb]:
                    planets_in_between.append(orb)
    planets_in_between = set(planets_in_between)
    planets_in_between = list(planets_in_between)
    planets_in_between.sort()
    planets_to_return = []
    for planet in planets_in_between:
        if reverse(planet) in planets_in_between:
            planets_to_return.append(planet)
    planets_to_return.sort()
    return tuple(planets_to_return)