
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
    
    planets = {"Venus" : "Mercury", 
            "Mercury" : "Earth", 
            "Earth" : "Jupiter",
            "Jupiter" :"Saturn",
            "Saturn" :"Uranus",
            "Uranus" : "Neptune",
            "Neptune" : "Pluto"}
    
    def get_planet_data(planet):
        if planets[planet] in planets.keys():
            return planets[planet]
        else: return []
    
    def get_planet_orbit(name1, name2):
        orbit1 = get_planet_data(name1)
        orbit2 = get_planet_data(name2)
        orbit = [planet for planet in orbit1 if planet in orbit2]
        return sorted(orbit)
    
    return get_planet_orbit(planet1, planet2)

