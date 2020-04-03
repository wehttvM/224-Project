import matplotlib.pyplot as plt
from networkx import nx

# topology servers
# apache server
# data server
# SQL account server w/ hvac permissions & groups
# firewall - opensuse pfsense cisco
# backup server - hardened red hat backup?
# VM server
# transcoding server
# remote offsite backup
# printer server
# VPN Server

# loctations
# 10 locations for tier 1
East_Asia = 'Moscow, Russia'
Europe = 'London, England'
Australia = 'Melbourne, Australia'
South_America = 'Rio de Janeiro, Brazil'
Asia = 'Tokyo, Japan'
# 5 loactions for tier 2
North_America = 'Toronto, Canada'
Central_North = 'Chicago, United States of America'
Central_South = 'Houston, United States of America'
Central_East = 'Washington DC, United States of America'
# 1 loactation for tier 3
Central_West = 'San Fransisco, United States of America'
Node_List_tier_1 = [Central_West, Central_East, Central_South, Central_North, North_America, Asia, South_America, Australia, Europe, East_Asia]
Node_List_tier_2 = [Central_West, Central_East, Central_South, Central_North, North_America]
Node_List_tier_3 = [Central_West]
G = nx.Graph()
for x in range(0, len(Node_List_tier_1)):
    G.add_node(Node_List_tier_1[x])
    if x == 0:
        pass
    else:
        G.add_edge(Central_West, Node_List_tier_1[x])
nx.draw(G, with_labels=True)
plt.show()
