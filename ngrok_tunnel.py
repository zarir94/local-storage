from ngrok import Client

client=Client('2GGXHzElLNdLKXSkTC3OwZeorZ4_38vy5MpyfcQWbH1gfpmHR')

username='Administrator'
password='Windows@10'

tunnels=[]

for t in client.tunnels.list():
	if t.proto=='tcp':
		tunnels.append(t.public_url.replace('tcp://',''))

print("USERNAME\tPASSWORD\tTUNNEL")
for tunnel in tunnels:
	print(f"{username}\t{password}\t{tunnel}")

