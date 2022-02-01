import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',metavar='',help='IP of the target or domain. (Ex. google.com)')
parser.add_argument('-pl','--portlimit',metavar='',help='Number limit of the port scanning,(Ex. 1000)')
args = parser.parse_args()
