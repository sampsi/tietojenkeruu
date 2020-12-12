Alt-H1 *Tiedon keruu*



#### H4 Kuvaus
Tiedonkeruu ohjelma on tehty *Python 3.8.5* lla.
scipti kerää Suorittiminen lämpötilan,koneen käynissäolo ajan, "juuren" ,data" levyn vapaan tilan gigoina ja tallentaa ne muuttjiin,
jonka jälkeen lähettää arvot mqtt palvelimelle.

###### H6 käytetyt kirjastot:
	*time
	* psutil
	* os
	* paho-mqtt
	* time 
	* uptime 
###### H6 asennus

suorita päätteessä  git clone https://github.com/sampsi/tietojenkeruu ,jonka jälkeen siirry hakemistoon ja suorita sielä seuraavat pip3 install -r requirements.txt
odota et pip3 asentaa tarvittavat kirjasto.Muokkaa mqtt.py tiedostoon hostname="192.168.1.4" Kohdalle oma mqtt palvelimen osoite ja mahdollinen salasana,
Muokkaa deltsu/temp, deltsu/uptime, deltsu/juuri ja deltsu/data haluiksi tocikeiksi. 
Suorita sciprti python3 mqtt.py
