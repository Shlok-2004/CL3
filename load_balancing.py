servers=["server1","server2","server3"]

requests=int(input("enter the no of client requests:"))

print("round_robin load balancing")

for i in range(requests):
    server=servers[i%len(servers)]
    print(f"Request{i+1} assigned to {server}")

print("least connection load balancing")

connections={
    "server1":0,
    "server2":0,
    "server3":0
}
for i in range(requests):
    server=min(connections,key=connections.get)
    print(f"request{i+1} assigned to {server}")
    connections[server]+=1
