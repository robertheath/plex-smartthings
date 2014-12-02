import logging
import requests
import urllib


class smartthings:

    username = ''
    password = ''
    url_root = 'https://graph.api.smartthings.com/api'

    def __init__(self, username=None, password=None):
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(__name__)

        self.username = username
        self.password = password

    def make_request(self, url, params=None, method='GET', ):
        url = self.url_root + url
        self.log.debug(url)
        headers = {'Accept': 'application/json'}
        if params:
            params = urllib.urlencode(params, True).replace('+', '%20')
        if method == 'GET':
            r = requests.get(url, auth=(self.username, self.password), params=params, headers=headers)
        elif method == 'POST':
            r = requests.post(url, auth=(self.username, self.password), params=params, headers=headers)

        try:
            response = r.json()
        except:
            response = r.text

        return response

    def accounts(self):
        url = "/accounts"
        return self.make_request(url)

    def locations(self, account_id):
        url = "/accounts/" + account_id + "/locations"
        return self.make_request(url)

    def events(self, account_id, max=10, all=False, source=''):
        url = "/accounts/" + account_id + "/events"
        params = {'all': all, 'source': source, 'max': max}
        return self.make_request(url, params=params)

    def hubs(self):
        url = "/hubs"
        return self.make_request(url)

    def hub(self, hub_id):
        url = "/hubs/" + hub_id
        return self.make_request(url)

    def hub_events(self, hub_id, max=10, all=False, source=None):
        url = "/hubs/" + hub_id + "/events"
        params = {'all': all, 'source': source, 'max': max}
        return self.make_request(url, params=params)

    def hub_devices(self, hub_id):
        url = "/hubs/" + hub_id + "/devices"
        return self.make_request(url)

    def device(self, device_id):
        url = "/devices/" + device_id
        return self.make_request(url)

    def device_events(self, device_id, max=10, all=False, source=None):
        url = "/devices/" + device_id + "/events"
        params = {'all': all, 'source': source, 'max': max}
        return self.make_request(url, params=params)

    def device_roles(self, device_id):
        url = "/devices/" + device_id + "/roles"
        return self.make_request(url)

    def device_types(self):
        url = "/devicetypes"
        return self.make_request(url)
