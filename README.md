# How to adapt this bot for your use

The prerequisites:

```
pip3 install Mastodon.py
pip3 install cairosvg
```

## First, create a bot account and set everything up

Create a [Mastodon Bot](https://tinysubversions.com/notes/mastodon-bot/).
You need to save the three codes you got as follows:

The *Client ID* and *Client Secret* go into the first file, each on a
line of its own. The filename is `<account>.client`, for example
`textmapper@botsin.space.client`.

Example content:

```
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
```

The *Access Token* goes to a separate file called `<account>.user`,
for example `textmapper@botsin.space.user`..

Example content:

```
7890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456
```

## Next, take a look at the code

This is where we get the image, upload it and, and post a status for
it:

```
text = "#textmapper #hex #map #rpg"
png = cairosvg.svg2png(url="https://campaignwiki.org/text-mapper/alpine/random")
media = mastodon.media_post(png, mime_type="image/png", description="a hex map")
mastodon.status_post(text, media_ids=[media.id])
```

If you want to change anything, it's probably going to be here.

## Finally, invoke it

This is what I do:

```
./bots.py textmapper@botsin.space
```
