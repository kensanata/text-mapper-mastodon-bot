#!/usr/bin/env python3
# Copyright (C) 2018  Alex Schroeder <alex@gnu.org>

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

from mastodon import Mastodon
import sys
import os.path
import urllib.request
import cairosvg
import re

def login(account, scopes = ['read', 'write']):
    """
    Login to your Mastodon account
    """

    (username, domain) = account.split("@")

    url = 'https://' + domain
    client_secret = account + '.client'
    user_secret = account + '.user'
    mastodon = None

    if not os.path.isfile(client_secret):
        print("Error: you need to create the file '%s'" % client_secret,
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(user_secret):
        print("Error: you need to create the file '%s'" % user_secret,
              file=sys.stderr)
        sys.exit(1)

    mastodon = Mastodon(
        client_id = client_secret,
        access_token = user_secret,
        api_base_url = url)

    return mastodon
    
def main():
    if len(sys.argv) == 1:
        print("Error: you must provide an account", file=sys.stderr)
        sys.exit(1)
    mastodon = login(sys.argv[1])
    url = "https://campaignwiki.org/text-mapper/alpine/random"
    text = "#textmapper #hex #map #rpg"
    # download SVG
    opener = urllib.request.FancyURLopener({})
    url = "https://campaignwiki.org/text-mapper/alpine/random"
    f = opener.open(url)
    svg = f.read()
    # extract seed and prepend it to the status text
    match = re.search("# Seed: (\d+)", svg.decode("utf-8"))
    if match:
        seed = match.group(1)
        text = url + "?seed=" + seed + " " + text
    # convert SVG to PNG
    png = cairosvg.svg2png(url=url)
    # upload image
    media = mastodon.media_post(png, mime_type="image/png", description="a hex map")
    # post status
    mastodon.status_post(text, media_ids=[media.id])

if __name__ == "__main__":
    main()