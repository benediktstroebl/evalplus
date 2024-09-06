
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
    import sys
    import ast
    import time
    #t = time.perf_counter()
    #planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    #planet_dict = {planet_names[i]: get_planet(planet_names[i]) for i in range(8)}
    #planets = [p for p in planet_dict if planet_dict[p] is not None]
    #if planet1 not in planets or planet2 not in planets:
    #   return tuple()
    #planet1_pos = planets.index(planet1)
    #planet2_pos = planets.index(planet2)
    #if planet2_pos < planet1_pos:
    #   planet1_pos, planet2_pos = planet2_pos, planet1_pos
    #planet2_orbit = planet_dict[planet2]
    #nt_list = []
    #for planet in planets[planet1_pos:planet2_pos+1]:
    #    if planet_dict[planet] is not None:
    #        for nt in planet_dict[planet].get_orbits():
    #            nt_list.append(nt)
    #orbit_list = [orbit for orbit in nt_list if orbit.get_pos() > planet2_orbit.get_pos()]
    #orbit_list.sort(key=lambda orbit: orbit.get_pos())
    #orb_list = []
    #for orbit in orbit_list:
    #   if orbit.get_pos() < planet2_orbit.get_pos():
    #       orb_list.append(orbit.get_pos())
    #orb_list.sort()
    #orb_list.pop(0)
    #return tuple(orb_list)

    planets = ast.literal_eval(open("data.txt").read())
    planet_dict = {planets[i].get_name(): planets[i] for i in range(len(planets))}
    planets = list(planet_dict.keys())
    if planet1 not in planets or planet2 not