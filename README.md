#  *Tiedon keruu*



##  Kuvaus
Tiedonkeruuohjelma on tehty *Python 3.8.5* lla.
scipti kerää Suorittiminen lämpötilan, koneen käynissäoloajan, "juuren" ,data" levyn vapaan tilan gigoina ja tallentaa ne muuttujiin,
jonka jälkeen lähettää arvot mqtt palvelimelle.

käytetyt kirjastot:
	* time
	* psutil
	* os
	* paho-mqtt
	* time 
	* uptime 

##  asennus

suorita päätteessä  `git clone https://github.com/sampsi/tietojenkeruu` ,jonka jälkeen siirry hakemistoon ja suorita sielä seuraavat `pip3 install -r requirements.txt`
odota, että pip3 asentaa tarvittavat kirjastot. 

Muokkaa`mqtt.py` tiedostoon `hostname="192.168.1.4"` Kohdalle oma mqtt palvelimen osoite ja mahdollinen salasana,
Muokkaa `deltsu/temp, deltsu/uptime, deltsu/juuri ja deltsu/data` haluiksi tocikeiksi. 
Suorita sciprti `python3 mqtt.py`

