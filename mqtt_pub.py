import paho.mqtt.client as mqttClient
import time
from mqtt_usu import usu
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address  = usu['broker_address'] #Broker address
port            = usu['port']           #Broker port
user            = usu['user']           #Connection username
password        = usu['password']       #Connection password
 
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    while True:
 
        value = input('Enter the message:')
        client.publish("python/test",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()