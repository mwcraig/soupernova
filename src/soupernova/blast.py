from astrowidgets import ImageWidget
from astropy.nddata import CCDData
import anywidget
import ipywidgets as ipw

DEFAULT_FILE = "http://physics.mnstate.edu/craig/ey-uma-S001-R001-C037-rp.fit.gz"


class Detonator(anywidget.AnyWidget):
    _esm = """
    import confetti from "https://esm.sh/canvas-confetti@1";
    function printMousePos(event) {
        console.log("EVENT");
        console.log(event);
        console.log(
            "clientX: " + event.layerX / event.view.outerWidth +
            " - clientY: " + event.layerY / event.view.outerHeight);
        //return {x: event.layerX, y: event.layerY};
        var moo = document.querySelectorAll('[role="main"]');
        console.log(moo);
        var origin = {
            x: event.clientX / moo[0].clientWidth,
            y: event.clientY / moo[0].clientHeight
        };
        console.log(origin);
        var poo = document.querySelectorAll("img.lm-Widget");
        console.log(poo);
        console.log(poo[0].isEqualNode(event.srcElement))
        if (poo[0].isEqualNode(event.srcElement)) {
           confetti({origin: origin, spread: 360, shapes: ['star']});
        }
    }

    function render({ model, el }) {
        var canvas = document.getElementById('my-canvas');
        console.log(canvas);
        console.log("Hello");

        document.addEventListener("click", printMousePos);

    }
    export default { render };
    """


class SouperNova(ipw.VBox):
    def __init__(self, *args, file=None, **kwargs):
        super().__init__(*args, *kwargs)
        if file is None:
            file = DEFAULT_FILE
        ccd = CCDData.read(file, cache=True)
        self.sn = Detonator()
        self.iw = ImageWidget()
        self.iw.load_nddata(ccd)
        self.children = [self.iw, self.sn]
