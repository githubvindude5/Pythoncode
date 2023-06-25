desc = ["\"first - prx70c\"","\"second - prx70c\"","\"third - prx70c\""]
port = ["8", "2", "3"]
agg = ["ae8", "ae2", "ae3"]

for i, element in enumerate(desc):

    print("set interfaces "+agg[i]+" description "+element+"")
    print("set interfaces "+agg[i]+" native-vlan-id 670")
    print("set interfaces "+agg[i]+" aggregated-ether-options lacp active")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching interface-mode trunk")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members c-man")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members c-lb")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-baha")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-doha")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-bzla")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-pbha")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-mlea")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-ktma")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-mcta")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-cmba")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-dela")
    print("set interfaces "+agg[i]+" unit 0 family ethernet-switching vlan members vvppoopp-blra")

    print("delete interfaces "+agg[i]+" disable")

    print("set interfaces ge-0/0/"+port[i]+" description "+element+"")
    print("set interfaces ge-0/0/"+port[i]+" ether-options 802.3ad lacp force-up")
    print("set interfaces ge-0/0/"+port[i]+" ether-options 802.3ad "+agg[i]+"")

    print("set interfaces ge-1/0/"+port[i]+" description "+element+"")
    print("set interfaces ge-1/0/"+port[i]+" ether-options 802.3ad "+agg[i]+"")
    print("\n")
