# DeepBeerLevelz

DISCLAIMER: No beer was wasted in the making of this project.

## Motivation

I was enjoying drinks with a friend at my flat and were drinking a particularly exceptional lambic beer (Cantillon Brabantiae, 2018. See: https://www.cantillon.be/) and wanted to ensure to distribute it as equitatively as possible.

Unfortunately I've never made the habit of buying glasses and thus have no matching glasses and just a collection of small missmatched glasses and jars. We tried our best to be equitative by timing the time of pouring with a consistent stream size rather than by judging the volume. We took this approach because we knew that evaluating volume can be deceptive, especially with nonlinear shaped glasses such as some of mine [Pechey et al, (2015). *PLoS One*. 10(12):e0144536. https://doi.org/10.1371/journal.pone.0144536]:

<img src="notebook_images/wine_glasses.png" alt="Glasses_wine" style="width: 600px;"/>

We further reasoned that as this is a 750ml beer bottle. If we were off by a relatively small amount, say one person received 120ml and the other 100ml. The more small glasses we had, the larger the disparity of consumption we would have if the difference between servings remained consistent. Indeed for this particular bottle, it would mean that one person would consume on average 20% more than the other. In the end we consumed two 750ml bottles, if one consumed 20% more than the other. Following the simple formula

$$
x + 1.2*x = 1500ml
$$

One can find that in the end one person drinks 681ml, while the other drinks 818ml, a full 147ml more than the other, more than a full glass!

In the end we got distracted by other topics and estimated our servings, yet the question stuck with me for a couple of days. Then I wondered, could I device a computer vision model that accurately returns the volume in the glass? I thought it could be a fun regression problem, upon researching further I found that there are comparatively few computer vision deep neural network models solving regression than classification or detection problems. I am not sure if there are simply overall less such problems to solve or there is something about them that makes them more troublesome.

I have a webcam, and I can train the model with accurate measurements, so let's give it a go.