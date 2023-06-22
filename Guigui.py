vbkeyword012023 15h01 new repo
vbkeyword012023 15h07


function post(el, cmd) {
    try {
        el.contentWindow.postMessage(JSON.stringify(assign({event: 'command'}, cmd)), '*');
    } catch (e) {}
}
