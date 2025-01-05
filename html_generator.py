import string
from textwrap import wrap
from applicationInnards import appData


def main():
    profile = r'https://raw.githubusercontent.com/Memory-Overload/luzs-laptop/refs/heads/main/images/luz%20cropped.jpg'
    with open('index.html', 'w') as f:
        # open html and add head to import css
        f.write(
            '<html><head><link rel="stylesheet" type="text/css" href="style.css"></head>')

        # open body
        f.write('<body>')

        # open container
        f.write('<div class="container">')
# region: login pages
        # add login pages
        password = 'AMITY'
        for i in range(5):
            # login screen with variable *'s
            f.write(f'<p class="hide"><a name="{password[:i] or "_"}">\
                    </a></p>')
            f.write(f'<div class="page">')
            f.write(
                f'<img src="{profile}" alt="Luz\'s about the author picture" class="profile">')
            f.write('<h1 class="user">Welcome, Good Witch Luz :)</h1>')
            f.write(f'<div class="passwordBox">\
                    {"*"*(i) or "Enter your password..."}</div>')

            # keyboard
            f.write('<div class="keyboard">')
            f.write('<table>')
            f.write('<thead></thead>')
            f.write('<tbody>')
            for group in wrap(string.ascii_uppercase, width=9):
                f.write('<tr>')
                lastGroup = group
                for char in group:
                    url = 'incorrect' + str(i+1)
                    if char == password[i]:
                        url = password[:i+1]
                    # user fully typed password
                    if 'AMITY' in url:
                        url = 'desktop'
                    f.write(f'<td><a \
                            href="#{url}" title="Press a key" class="key">{char}</a></td>')
                if len(lastGroup) == 8:
                    f.write('<td><a href="#_" title="Clear" class="key">Clear\
                            </a></td>')
                f.write('</tr>')
            f.write('</tbody>')
            f.write('</table>')
            f.write('</div>')
            f.write(
                '<details><summary>Hint</summary><p>Sweet potato</p></details>')
            f.write('</div>')

        # incorrect pages for login
        for i in range(6):

            # login screen with variable *'s
            f.write(f'<p class="hide"><a name="incorrect{i}"></a></p>')
            f.write(f'<div class="page">')
            f.write(
                f'<img src="{profile}" alt="Luz\'s about the author picture" class="profile">')
            f.write('<h1 class="user">Welcome, Good Witch Luz :)</h1>')
            f.write(f'<div class="passwordBox">\
                    {"*"*(i) or "Enter your password..."}</div>')

            # keyboard
            f.write('<div class="keyboard">')
            f.write('<table>')
            f.write('<thead></thead>')
            f.write('<tbody>')
            for group in wrap(string.ascii_uppercase, width=9):
                f.write('<tr>')
                lastGroup = group
                for char in group:
                    url = 'incorrect' + str(i+1)
                    if i == 5:
                        url = "_"
                    f.write(f'<td><a \
                            href="#{url}" title="Press a key" class="key">{char}</a></td>')
                if len(lastGroup) == 8:
                    f.write('<td><a href="#_" title="Clear" class="key">Clear\
                            </a></td>')
                f.write('</tr>')
            f.write('</tbody>')
            f.write('</table>')
            f.write('</div>')
            f.write(
                '<details><summary>Hint</summary><p>Sweet potato</p></details>')
            f.write('</div>')
# endregion: login pages
# region: desktop
        # open desktop
        f.write('<p class="hide"><a name="desktop"></a></p>')
        f.write('<div class="page" id="desktop">')
        f.write('<div class="wallpaperOverlay">')
        f.write('<a><div></div></a>')
        apps = ["video", "stuff", "webBrowser", "moonFarmValley",
                "hollerKnight", "hades", "GWAFic", "uMovie"]
        for app in apps:
            f.write(f'<a href="#{app}"><div class="icon {app}">\
                    </div></a>')
        # close wallpaper overlay
        f.write('</div>')
        # close desktop
        f.write('</div>')
# endregion: desktop
# region: applications
        for app in apps:
            underConstruction = f'<h1>{app} is under construction!\
                </h1><p><a href="#desktop">Back to desktop</a></p>'
            f.write(f'<p class="hide"><a name="{app}"></a></p>')
            f.write(f'<div class="page" id="{app}">')
            f.write('<div class="wallpaperOverlay">')
            f.write('<div class="maximizedApp">')
            f.write(appData[app] or underConstruction)
            f.write('</div>')  # maximizedApp
            f.write('</div>')  # wallpaperOverlay
            f.write('</div>')  # page

# endregion: applications
        # close container
        f.write('</div>')

        # close body and html
        f.write('</body></html>')


if __name__ == '__main__':
    main()
