
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    def nearest_planet(name):
        return planets.index(name)

    def minimum(a, b, c):
        return a if abs(a-nearest_planet(planet1)) < abs(b-nearest_planet(planet1)) else b

    def maximum(a, b, c):
        return a if abs(a-nearest_planet(planet2)) > abs(b-nearest_planet(planet2)) else b
    
    def between(a, b, c):
        return (nearest_planet(a), nearest_planet(b), nearest_planet(c))    
    
    def orbit(name):
        return (nearest_planet(name), name)
    
    def orbit_range(name1, name2):
        return tuple(set(between(name1, name2, name)) for name in planets)
    
    def orbit_count(planet):
        return len(set(between(planet, planet, planet2)) - set(planet))
    
    orbit_list = tuple(map(orbit, planets))
    minimum_planet = minimum(*orbit_list)
    maximum_planet = maximum(*orbit_list)
    name_range = orbit_range(minimum_planet, maximum_planet)
    return tuple(sorted(set(planet for planet in planets if planet_count(planet) == 8) - set(name_range)))
